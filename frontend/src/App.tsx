import { useEffect, useRef, useState } from 'react'
import { listSources, search } from './api'
import type { SearchResponse, SourceMeta, SourceResult, StoryEntity } from './types'
import { EntityCard } from './components/EntityCard'
import { DetailReader } from './components/DetailReader'
import { ResultsSkeleton } from './components/Skeletons'
import { LicenseBadge } from './components/Badges'
import { ComposeView } from './components/ComposeView'
import { LibraryView } from './components/LibraryView'
import { useCollection, type Collection } from './hooks/useCollection'
import { typeLabel } from './meta'
import './App.css'

const EXAMPLES = ['gilgamesh', 'dragon', '조선', 'Odysseus', '구미호', 'samurai', 'angel']
type View = 'discover' | 'library' | 'sources' | 'compose'

export default function App() {
  const [view, setView] = useState<View>('discover')
  const [sources, setSources] = useState<SourceMeta[]>([])
  const [selected, setSelected] = useState<Set<string>>(new Set())
  const [query, setQuery] = useState('')
  const [data, setData] = useState<SearchResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [active, setActive] = useState<StoryEntity | null>(null)
  const abortRef = useRef<AbortController | null>(null)
  const collection = useCollection()

  useEffect(() => {
    listSources()
      .then((r) => setSources(r.sources))
      .catch(() =>
        setError('백엔드(/api/sources)에 연결할 수 없습니다. uvicorn이 실행 중인지 확인하세요.'),
      )
  }, [])

  async function runSearch(q: string) {
    const term = q.trim()
    if (!term) return
    setView('discover')
    abortRef.current?.abort()
    const ac = new AbortController()
    abortRef.current = ac
    setLoading(true)
    setError(null)
    try {
      const res = await search(term, {
        sources: selected.size ? [...selected] : undefined,
        limit: 12,
        signal: ac.signal,
      })
      setData(res)
    } catch (e) {
      if ((e as Error).name !== 'AbortError') setError((e as Error).message)
    } finally {
      setLoading(false)
    }
  }

  function toggleSource(id: string) {
    setSelected((prev) => {
      const next = new Set(prev)
      if (next.has(id)) next.delete(id)
      else next.add(id)
      return next
    })
  }

  return (
    <div className="app">
      <nav className="nav">
        <button className="brand" onClick={() => setView('discover')}>
          <span className="brand-mark">❦</span> StoryAPIs
        </button>
        <div className="nav-tabs">
          <button
            className={`nav-tab ${view === 'discover' ? 'on' : ''}`}
            onClick={() => setView('discover')}
          >
            발견
          </button>
          <button
            className={`nav-tab ${view === 'library' ? 'on' : ''}`}
            onClick={() => setView('library')}
          >
            보관함
          </button>
          <button
            className={`nav-tab ${view === 'sources' ? 'on' : ''}`}
            onClick={() => setView('sources')}
          >
            소스 <span className="nav-count">{sources.length}</span>
          </button>
          <button
            className={`nav-tab ${view === 'compose' ? 'on' : ''}`}
            onClick={() => setView('compose')}
          >
            집필 <span className="nav-count">{collection.count}</span>
          </button>
        </div>
      </nav>

      {view === 'discover' && (
        <Discover
          query={query}
          setQuery={setQuery}
          runSearch={runSearch}
          sources={sources}
          selected={selected}
          toggleSource={toggleSource}
          clearSelected={() => setSelected(new Set())}
          data={data}
          loading={loading}
          error={error}
          onOpen={setActive}
          collection={collection}
        />
      )}

      {view === 'sources' && (
        <SourcesView
          sources={sources}
          onSearchSource={(id) => {
            setSelected(new Set([id]))
            setView('discover')
          }}
        />
      )}

      {view === 'library' && (
        <LibraryView
          collection={collection}
          onOpen={setActive}
          onCompose={() => setView('compose')}
        />
      )}

      {view === 'compose' && (
        <ComposeView collection={collection} onDiscover={() => setView('discover')} />
      )}

      {active && (
        <DetailReader
          entity={active}
          onClose={() => setActive(null)}
          inCollection={collection.has(active.id)}
          onToggleCollect={() => collection.toggle(active)}
        />
      )}

      <footer className="foot">
        세계의 역사·신화·문학을 모으는 이야기의 원천 ·{' '}
        <a href="https://github.com/squall321/StoryAPIs" target="_blank" rel="noreferrer">
          GitHub
        </a>
      </footer>
    </div>
  )
}

function Discover(props: {
  query: string
  setQuery: (v: string) => void
  runSearch: (q: string) => void
  sources: SourceMeta[]
  selected: Set<string>
  toggleSource: (id: string) => void
  clearSelected: () => void
  data: SearchResponse | null
  loading: boolean
  error: string | null
  onOpen: (e: StoryEntity) => void
  collection: Collection
}) {
  const {
    query,
    setQuery,
    runSearch,
    sources,
    selected,
    toggleSource,
    clearSelected,
    data,
    loading,
    error,
    onOpen,
    collection,
  } = props

  return (
    <main className="wrap">
      <header className="hero">
        <h1 className="hero-title">이야기의 원천을 찾다</h1>
        <p className="hero-sub">
          세계의 역사·신화·문학·유물 — {sources.length || '여러'}개 지식 소스를 한 번에 검색합니다.
        </p>
        <form
          className="searchbar"
          onSubmit={(e) => {
            e.preventDefault()
            runSearch(query)
          }}
        >
          <input
            autoFocus
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="검색어를 입력하세요  ·  예: 조선, dragon, Gilgamesh"
            aria-label="search"
          />
          <button type="submit" disabled={loading}>
            {loading ? '검색 중…' : '검색'}
          </button>
        </form>
        <div className="examples">
          {EXAMPLES.map((ex) => (
            <button
              key={ex}
              className="chip ghost"
              onClick={() => {
                setQuery(ex)
                runSearch(ex)
              }}
            >
              {ex}
            </button>
          ))}
        </div>
      </header>

      {sources.length > 0 && (
        <section className="filters">
          <span className="filters-label">소스 필터</span>
          {sources.map((s) => (
            <button
              key={s.id}
              className={`chip ${selected.has(s.id) ? 'active' : ''}`}
              title={`${s.description}\n라이선스: ${s.license.name}`}
              onClick={() => toggleSource(s.id)}
            >
              {s.name}
            </button>
          ))}
          {selected.size > 0 && (
            <button className="chip ghost clear" onClick={clearSelected}>
              전체 ✕
            </button>
          )}
        </section>
      )}

      {error && <div className="error">{error}</div>}

      {loading && <ResultsSkeleton />}

      {!loading && data && (
        <section className="results">
          <div className="results-meta">
            <strong>{data.total_hits}</strong>건 · {data.elapsed_ms}ms · &ldquo;{data.query}&rdquo;
          </div>
          {data.results.map((r) => (
            <SourceGroup key={r.source_id} result={r} onOpen={onOpen} collection={collection} />
          ))}
          {data.total_hits === 0 && (
            <p className="empty">결과가 없습니다. 다른 검색어를 시도해 보세요.</p>
          )}
        </section>
      )}

      {!loading && !data && !error && (
        <section className="splash">
          <p>검색어를 입력하면 모든 지식 소스에서 동시에 자료를 모아옵니다.</p>
        </section>
      )}
    </main>
  )
}

function SourceGroup({
  result,
  onOpen,
  collection,
}: {
  result: SourceResult
  onOpen: (e: StoryEntity) => void
  collection: Collection
}) {
  if (result.error) {
    return (
      <section className="source-group">
        <div className="group-head">
          <h2>{result.source_name}</h2>
          <span className="group-note err">일시적으로 응답하지 않음</span>
        </div>
      </section>
    )
  }
  if (!result.hits.length) return null
  return (
    <section className="source-group">
      <div className="group-head">
        <h2>{result.source_name}</h2>
        <span className="group-note">
          {result.total}건 · {result.elapsed_ms}ms
        </span>
      </div>
      <div className="cards">
        {result.hits.map((h) => (
          <EntityCard
            key={h.entity.id}
            hit={h}
            onOpen={(hit) => onOpen(hit.entity)}
            inCollection={collection.has(h.entity.id)}
            onCollect={(e) => collection.toggle(e)}
          />
        ))}
      </div>
    </section>
  )
}

function SourcesView({
  sources,
  onSearchSource,
}: {
  sources: SourceMeta[]
  onSearchSource: (id: string) => void
}) {
  return (
    <main className="wrap">
      <header className="hero compact">
        <h1 className="hero-title">지식 소스 {sources.length}곳</h1>
        <p className="hero-sub">각 소스의 범위·언어·라이선스를 확인하고 바로 검색하세요.</p>
      </header>
      <div className="source-grid">
        {sources.map((s) => (
          <article key={s.id} className="source-card">
            <div className="source-card-head">
              <h3>{s.name}</h3>
              <LicenseBadge license={s.license} />
            </div>
            <p className="source-desc">{s.description}</p>
            <div className="source-tags">
              {s.entity_types.slice(0, 5).map((t) => (
                <span key={t} className="mini">
                  {typeLabel(t)}
                </span>
              ))}
              {s.languages.slice(0, 4).map((l) => (
                <span key={l} className="mini lang">
                  {l}
                </span>
              ))}
              {s.auth_required && <span className="mini auth">API 키 필요</span>}
            </div>
            <div className="source-card-foot">
              <button className="src-btn" onClick={() => onSearchSource(s.id)}>
                이 소스로 검색
              </button>
              {s.homepage && (
                <a href={s.homepage} target="_blank" rel="noreferrer">
                  홈페이지 ↗
                </a>
              )}
            </div>
          </article>
        ))}
      </div>
    </main>
  )
}
