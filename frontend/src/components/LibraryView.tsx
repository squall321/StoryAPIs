import { useEffect, useRef, useState } from 'react'
import { librarySearch, libraryStats } from '../api'
import type { LibraryStats, StoryEntity } from '../types'
import type { Collection } from '../hooks/useCollection'
import { EntityCard } from './EntityCard'
import { ResultsSkeleton } from './Skeletons'

// Browses the locally collected (ingested) corpus — not a live API call.
export function LibraryView({
  collection,
  onOpen,
}: {
  collection: Collection
  onOpen: (e: StoryEntity) => void
}) {
  const [stats, setStats] = useState<LibraryStats | null>(null)
  const [q, setQ] = useState('')
  const [source, setSource] = useState<string | null>(null)
  const [items, setItems] = useState<StoryEntity[] | null>(null)
  const [loading, setLoading] = useState(false)
  const abortRef = useRef<AbortController | null>(null)

  useEffect(() => {
    libraryStats().then(setStats).catch(() => setStats(null))
    void run('', null)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  async function run(nextQ: string, nextSource: string | null) {
    abortRef.current?.abort()
    const ac = new AbortController()
    abortRef.current = ac
    setLoading(true)
    try {
      const r = await librarySearch({
        q: nextQ.trim() || undefined,
        source: nextSource ?? undefined,
        limit: 60,
        signal: ac.signal,
      })
      setItems(r.items)
    } catch (e) {
      if ((e as Error).name !== 'AbortError') setItems([])
    } finally {
      setLoading(false)
    }
  }

  function pickSource(id: string | null) {
    setSource(id)
    void run(q, id)
  }

  const sources = stats ? Object.entries(stats.by_source) : []

  return (
    <main className="wrap">
      <header className="hero compact">
        <h1 className="hero-title">보관함 · 수집한 데이터</h1>
        <p className="hero-sub">
          {stats
            ? `로컬에 수집·저장된 ${stats.total.toLocaleString()}건 (전문 ${stats.with_fulltext}건) — 라이브 호출 없이 검색합니다.`
            : '수집된 데이터를 불러오는 중…'}
        </p>
        <form
          className="searchbar"
          onSubmit={(e) => {
            e.preventDefault()
            void run(q, source)
          }}
        >
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="수집한 자료 안에서 검색  ·  예: 실록, dragon, 용"
            aria-label="library search"
          />
          <button type="submit" disabled={loading}>
            검색
          </button>
        </form>
      </header>

      {stats && stats.total === 0 && (
        <div className="notice">
          아직 수집된 데이터가 없습니다. 백엔드에서{' '}
          <code>.venv/Scripts/python.exe scripts/ingest.py</code> 를 실행해 수집하세요.
        </div>
      )}

      {sources.length > 0 && (
        <section className="filters">
          <span className="filters-label">소스</span>
          <button
            className={`chip ${source === null ? 'active' : ''}`}
            onClick={() => pickSource(null)}
          >
            전체 {stats?.total}
          </button>
          {sources.map(([id, n]) => (
            <button
              key={id}
              className={`chip ${source === id ? 'active' : ''}`}
              onClick={() => pickSource(id)}
            >
              {id} {n}
            </button>
          ))}
        </section>
      )}

      {loading && <ResultsSkeleton groups={1} cards={8} />}

      {!loading && items && (
        <section className="results">
          <div className="results-meta">
            <strong>{items.length}</strong>건 표시
            {source && ` · ${source}`}
            {q.trim() && ` · "${q.trim()}"`}
          </div>
          {items.length === 0 ? (
            <p className="empty">해당하는 자료가 없습니다.</p>
          ) : (
            <div className="cards">
              {items.map((e) => (
                <EntityCard
                  key={e.id}
                  hit={{ entity: e }}
                  onOpen={(hit) => onOpen(hit.entity)}
                  inCollection={collection.has(e.id)}
                  onCollect={(ent) => collection.toggle(ent)}
                />
              ))}
            </div>
          )}
        </section>
      )}
    </main>
  )
}
