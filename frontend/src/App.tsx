import { useEffect, useRef, useState } from 'react'
import { listSources, search } from './api'
import type { SearchResponse, SourceMeta, SourceResult, StoryEntity } from './types'
import './App.css'

const EXAMPLES = ['gilgamesh', 'dragon', 'Joseon', 'Odysseus', '구미호', 'samurai']

export default function App() {
  const [sources, setSources] = useState<SourceMeta[]>([])
  const [selected, setSelected] = useState<Set<string>>(new Set())
  const [query, setQuery] = useState('')
  const [data, setData] = useState<SearchResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const abortRef = useRef<AbortController | null>(null)

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
      <header className="hero">
        <h1>📚 StoryAPIs</h1>
        <p className="tagline">
          세계의 역사·신화·문학을 한 번에 — 이야기의 원천을 모으는 지식 보고
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
            placeholder="검색어를 입력하세요 (예: 조선, dragon, Gilgamesh)"
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
        <section className="sources">
          <span className="sources-label">소스 필터:</span>
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
            <button className="chip ghost" onClick={() => setSelected(new Set())}>
              전체 ✕
            </button>
          )}
        </section>
      )}

      {error && <div className="error">{error}</div>}

      {data && (
        <section className="results">
          <div className="results-meta">
            <strong>{data.total_hits}</strong>건 · {data.elapsed_ms}ms · &ldquo;{data.query}&rdquo;
          </div>
          {data.results.map((r) => (
            <SourceBlock key={r.source_id} result={r} />
          ))}
        </section>
      )}

      {!data && !error && (
        <section className="empty">
          <p>
            검색어를 입력하면 {sources.length || '여러'}개 지식 소스에서 동시에 자료를 모아옵니다.
          </p>
        </section>
      )}
    </div>
  )
}

function SourceBlock({ result }: { result: SourceResult }) {
  if (result.error) {
    return (
      <div className="source-block">
        <h2>
          {result.source_name} <span className="muted">— 일시 오류</span>
        </h2>
        <p className="source-error">{result.error}</p>
      </div>
    )
  }
  if (!result.hits.length) return null
  return (
    <div className="source-block">
      <h2>
        {result.source_name}{' '}
        <span className="muted">
          ({result.total} · {result.elapsed_ms}ms)
        </span>
      </h2>
      <div className="cards">
        {result.hits.map((h) => (
          <EntityCard key={h.entity.id} entity={h.entity} snippet={h.snippet} />
        ))}
      </div>
    </div>
  )
}

function EntityCard({ entity, snippet }: { entity: StoryEntity; snippet?: string | null }) {
  const img = entity.media[0]?.thumbnail_url || entity.media[0]?.url
  return (
    <article className="card">
      {img && <img className="card-img" src={img} alt="" loading="lazy" />}
      <div className="card-body">
        <div className="card-head">
          <span className={`type type-${entity.type}`}>{entity.type}</span>
          {entity.time?.label && <span className="time">{entity.time.label}</span>}
        </div>
        <h3 className="card-title">
          {entity.provenance.source_url ? (
            <a href={entity.provenance.source_url} target="_blank" rel="noreferrer">
              {entity.title}
            </a>
          ) : (
            entity.title
          )}
        </h3>
        {entity.summary && <p className="card-summary">{entity.summary}</p>}
        {snippet && <p className="card-snippet">“{snippet}”</p>}
        {entity.tags.length > 0 && (
          <div className="tags">
            {entity.tags.slice(0, 6).map((t, i) => (
              <span key={i} className="tag">
                {t}
              </span>
            ))}
          </div>
        )}
        <div className="card-foot">
          <span className="lic">{entity.provenance.license.name}</span>
        </div>
      </div>
    </article>
  )
}
