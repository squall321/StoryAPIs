import { useState } from 'react'
import type { StoryEntity } from '../types'
import { typeLabel } from '../meta'

// A cover image that gracefully degrades to an elegant typographic banner
// whenever the entity has no usable media or the image fails to load.
export function Cover({
  entity,
  className,
  hero = false,
}: {
  entity: StoryEntity
  className?: string
  hero?: boolean
}) {
  const src = entity.media[0]?.thumbnail_url || entity.media[0]?.url || ''
  const [failed, setFailed] = useState(false)
  const showImage = Boolean(src) && !failed

  if (showImage) {
    return (
      <img
        className={`cover cover-img ${className ?? ''}`}
        src={src}
        alt={entity.media[0]?.caption ?? ''}
        loading="lazy"
        onError={() => setFailed(true)}
      />
    )
  }

  const initial = (entity.title.trim()[0] ?? '?').toUpperCase()
  return (
    <div
      className={`cover cover-fallback type-bg-${entity.type} ${className ?? ''}`}
      data-type={entity.type}
      aria-hidden
    >
      <span className="cover-glyph">{initial}</span>
      {hero && <span className="cover-kind">{typeLabel(entity.type)}</span>}
    </div>
  )
}
