import type { SearchHit } from '../types'
import { TypeBadge } from './Badges'
import { Cover } from './Cover'

export function EntityCard({ hit, onOpen }: { hit: SearchHit; onOpen: (hit: SearchHit) => void }) {
  const { entity, snippet } = hit
  return (
    <article className="card">
      <button
        type="button"
        className="card-hit"
        onClick={() => onOpen(hit)}
        aria-label={`${entity.title} 자세히 보기`}
      >
        <div className="card-cover">
          <Cover entity={entity} />
        </div>
        <div className="card-body">
          <div className="card-head">
            <TypeBadge type={entity.type} />
            {entity.time?.label && <span className="card-time">{entity.time.label}</span>}
          </div>
          <h3 className="card-title">{entity.title}</h3>
          {entity.summary && <p className="card-summary">{entity.summary}</p>}
          {!entity.summary && snippet && <p className="card-snippet">“{snippet}”</p>}
          {entity.tags.length > 0 && (
            <div className="card-tags">
              {entity.tags.slice(0, 6).map((t, i) => (
                <span key={i} className="tag">
                  {t}
                </span>
              ))}
            </div>
          )}
          <div className="card-foot">
            <span className="card-source">{entity.provenance.source_name}</span>
            <span className="card-dot" aria-hidden>
              ·
            </span>
            <span className="card-lic">{entity.provenance.license.name || '라이선스 미상'}</span>
          </div>
        </div>
      </button>
    </article>
  )
}
