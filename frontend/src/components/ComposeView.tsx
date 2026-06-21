import { useEffect, useRef, useState } from 'react'
import { compose, composeStatus } from '../api'
import type { ComposeOptions, ComposeResponse } from '../types'
import type { Collection } from '../hooks/useCollection'
import { TypeBadge } from './Badges'
import { TextSkeleton } from './Skeletons'

type State =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'done'; result: ComposeResponse }
  | { status: 'error'; message: string }

export function ComposeView({
  collection,
  onDiscover,
}: {
  collection: Collection
  onDiscover: () => void
}) {
  const [brief, setBrief] = useState('')
  const [options, setOptions] = useState<ComposeOptions>({ length: 'medium', language: 'ko' })
  const [state, setState] = useState<State>({ status: 'idle' })
  const [available, setAvailable] = useState<boolean | null>(null)
  const abortRef = useRef<AbortController | null>(null)

  useEffect(() => {
    composeStatus()
      .then((s) => setAvailable(s.available))
      .catch(() => setAvailable(null))
  }, [])

  async function run() {
    if (!brief.trim() || collection.items.length === 0) return
    abortRef.current?.abort()
    const ac = new AbortController()
    abortRef.current = ac
    setState({ status: 'loading' })
    try {
      const result = await compose(
        { brief: brief.trim(), entities: collection.items, options },
        ac.signal,
      )
      setState({ status: 'done', result })
    } catch (e) {
      if ((e as Error).name !== 'AbortError') {
        setState({ status: 'error', message: (e as Error).message })
      }
    }
  }

  return (
    <main className="wrap">
      <header className="hero compact">
        <h1 className="hero-title">수집한 자료로 이야기를 짓다</h1>
        <p className="hero-sub">
          모은 원천을 Claude(Opus 4.8)가 엮어 새 이야기 초안을 씁니다 — 출처를 인용한 채로.
        </p>
      </header>

      {available === false && (
        <div className="notice">
          작문 기능은 <code>STORYAPIS_ANTHROPIC_API_KEY</code> 가 설정되어야 동작합니다.
          <code>backend/.env</code> 에 키를 넣고 백엔드를 재시작하세요.
        </div>
      )}

      <section className="compose">
        <div className="compose-form">
          <label className="field">
            <span>무엇을 쓸까요?</span>
            <textarea
              value={brief}
              onChange={(e) => setBrief(e.target.value)}
              rows={4}
              placeholder="예: 수집한 자료를 바탕으로 용을 둘러싼 조선 궁중 미스터리 단편을 써줘"
            />
          </label>
          <div className="opt-row">
            <label className="field">
              <span>분량</span>
              <select
                value={options.length}
                onChange={(e) =>
                  setOptions({ ...options, length: e.target.value as ComposeOptions['length'] })
                }
              >
                <option value="short">짧게</option>
                <option value="medium">보통</option>
                <option value="long">길게</option>
              </select>
            </label>
            <label className="field">
              <span>언어</span>
              <select
                value={options.language}
                onChange={(e) =>
                  setOptions({
                    ...options,
                    language: e.target.value as ComposeOptions['language'],
                  })
                }
              >
                <option value="ko">한국어</option>
                <option value="en">English</option>
              </select>
            </label>
            <label className="field">
              <span>장르</span>
              <input
                value={options.genre ?? ''}
                onChange={(e) => setOptions({ ...options, genre: e.target.value })}
                placeholder="판타지, 사극…"
              />
            </label>
            <label className="field">
              <span>톤</span>
              <input
                value={options.tone ?? ''}
                onChange={(e) => setOptions({ ...options, tone: e.target.value })}
                placeholder="비장한, 유쾌한…"
              />
            </label>
          </div>
          <button
            className="compose-go"
            disabled={state.status === 'loading' || !brief.trim() || collection.items.length === 0}
            onClick={run}
          >
            {state.status === 'loading' ? '집필 중…' : '이야기 생성'}
          </button>
        </div>

        <aside className="compose-side">
          <div className="side-head">
            <h3>수집함 ({collection.count})</h3>
            {collection.count > 0 && (
              <button className="chip ghost" onClick={collection.clear}>
                비우기
              </button>
            )}
          </div>
          {collection.items.length === 0 ? (
            <p className="side-empty">
              아직 자료가 없습니다.{' '}
              <button className="linklike" onClick={onDiscover}>
                발견에서 자료를 담아보세요 →
              </button>
            </p>
          ) : (
            <ul className="side-list">
              {collection.items.map((e) => (
                <li key={e.id}>
                  <TypeBadge type={e.type} />
                  <span className="side-title">{e.title}</span>
                  <button
                    className="side-x"
                    onClick={() => collection.remove(e.id)}
                    aria-label="제거"
                  >
                    ✕
                  </button>
                </li>
              ))}
            </ul>
          )}
        </aside>
      </section>

      {state.status === 'loading' && (
        <section className="draft">
          <TextSkeleton />
        </section>
      )}

      {state.status === 'error' && (
        <div className="error">{state.message}</div>
      )}

      {state.status === 'done' && (
        <section className="draft">
          <article className="draft-doc">
            <div className="draft-text">{state.result.draft}</div>
          </article>
          {state.result.used_sources.length > 0 && (
            <div className="draft-sources">
              <h4>인용된 출처</h4>
              <ul>
                {state.result.used_sources.map((s) => (
                  <li key={s.id}>
                    {s.source_url ? (
                      <a href={s.source_url} target="_blank" rel="noreferrer">
                        {s.title}
                      </a>
                    ) : (
                      s.title
                    )}
                    <span className="muted"> · {s.source_name}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
          <p className="draft-meta">
            {state.result.model}
            {state.result.usage &&
              ` · ${state.result.usage.input_tokens}→${state.result.usage.output_tokens} tokens`}
          </p>
        </section>
      )}
    </main>
  )
}
