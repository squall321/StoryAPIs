import { useEffect, useState } from 'react'
import type { StoryEntity } from '../types'
import { fetchFullText } from '../api'
import { LicenseBadge, TypeBadge } from './Badges'
import { TextSkeleton } from './Skeletons'

type FT =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'loaded'; text: string; truncated: boolean }
  | { status: 'none' }
  | { status: 'error'; message: string }

// The "에피소드" reader: a slide-in drawer that presents one StoryEntity
// beautifully, lazily loading full text when the source can provide it.
export function DetailReader({ entity, onClose }: { entity: StoryEntity; onClose: () => void }) {
  const [ft, setFt] = useState<FT>({ status: 'idle' })

  useEffect(() => {
    setFt({ status: 'idle' })
  }, [entity.id])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    document.addEventListener('keydown', onKey)
    const prev = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.style.overflow = prev
    }
  }, [onClose])

  async function loadFullText() {
    setFt({ status: 'loading' })
    try {
      const r = await fetchFullText(entity.id)
      setFt({ status: 'loaded', text: r.text, truncated: r.truncated })
    } catch (e) {
      const msg = (e as Error).message
      setFt(msg.includes('404') ? { status: 'none' } : { status: 'error', message: msg })
    }
  }

  const img = entity.media[0]?.url || entity.media[0]?.thumbnail_url
  const places = entity.places.map((p) => p.label || p.country).filter(Boolean)
  const initial = (entity.title.trim()[0] ?? '?').toUpperCase()

  return (
    <div className="reader-overlay" onClick={onClose}>
      <aside
        className="reader"
        role="dialog"
        aria-modal="true"
        aria-label={entity.title}
        onClick={(e) => e.stopPropagation()}
      >
        <button className="reader-close" onClick={onClose} aria-label="닫기">
          ✕
        </button>

        <div className={`reader-hero ${img ? 'has-img' : `type-bg-${entity.type}`}`}>
          {img ? (
            <img src={img} alt={entity.media[0]?.caption ?? ''} />
          ) : (
            <span className="reader-hero-glyph">{initial}</span>
          )}
        </div>

        <div className="reader-body">
          <div className="reader-topline">
            <TypeBadge type={entity.type} />
            <span className="reader-source">{entity.provenance.source_name}</span>
          </div>

          <h1 className="reader-title">{entity.title}</h1>

          {(entity.time?.label || places.length > 0 || entity.languages.length > 0) && (
            <div className="reader-meta">
              {entity.time?.label && <span>🕑 {entity.time.label}</span>}
              {places.length > 0 && <span>📍 {places.join(', ')}</span>}
              {entity.languages.length > 0 && <span>🗣 {entity.languages.join(', ')}</span>}
            </div>
          )}

          {entity.summary && <p className="reader-summary">{entity.summary}</p>}
          {entity.description && <p className="reader-desc">{entity.description}</p>}

          <FullTextSection entity={entity} ft={ft} onLoad={loadFullText} />

          {entity.tags.length > 0 && (
            <div className="reader-tags">
              {entity.tags.map((t, i) => (
                <span key={i} className="tag">
                  {t}
                </span>
              ))}
            </div>
          )}

          <div className="reader-prov">
            <LicenseBadge license={entity.provenance.license} />
            {entity.provenance.source_url && (
              <a
                className="reader-link"
                href={entity.provenance.source_url}
                target="_blank"
                rel="noreferrer"
              >
                원문 보기 ↗
              </a>
            )}
          </div>
        </div>
      </aside>
    </div>
  )
}

function FullTextSection({
  entity,
  ft,
  onLoad,
}: {
  entity: StoryEntity
  ft: FT
  onLoad: () => void
}) {
  if (entity.full_text) {
    return (
      <div className="reader-doc">
        <div className="reader-text">{entity.full_text}</div>
      </div>
    )
  }
  switch (ft.status) {
    case 'idle':
      return (
        <button className="reader-load" onClick={onLoad}>
          전문 읽기
        </button>
      )
    case 'loading':
      return <TextSkeleton />
    case 'none':
      return <p className="reader-note">이 항목은 전문(全文)을 제공하지 않습니다.</p>
    case 'error':
      return <p className="reader-note">전문을 불러오지 못했습니다: {ft.message}</p>
    case 'loaded':
      return (
        <div className="reader-doc">
          <div className="reader-text">{ft.text}</div>
          {ft.truncated && (
            <p className="reader-trunc">
              일부만 표시했습니다 — 원문에서 계속 읽어보세요.
            </p>
          )}
        </div>
      )
  }
}
