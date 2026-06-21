import type { EntityType, License } from '../types'
import { licenseLabel, licenseTone, typeLabel } from '../meta'

export function TypeBadge({ type }: { type: EntityType }) {
  return (
    <span className={`type-badge type-${type}`} data-type={type}>
      {typeLabel(type)}
    </span>
  )
}

export function LicenseBadge({ license }: { license?: License | null }) {
  const tone = licenseTone(license)
  const label = licenseLabel(license)
  const title =
    license?.commercial_ok === true
      ? '상업적 이용 가능'
      : license?.commercial_ok === false
        ? '상업적 이용 제한'
        : '이용 조건 확인 필요'
  return (
    <span className={`lic-badge lic-${tone}`} title={`${label} · ${title}`}>
      <span className="lic-dot" aria-hidden />
      {label}
    </span>
  )
}
