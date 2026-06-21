import type { EntityType, License } from './types'

// Korean labels for each entity type, used in badges and banners.
export const TYPE_LABEL: Record<EntityType, string> = {
  person: '인물',
  place: '장소',
  event: '사건',
  period: '시대',
  work: '작품',
  deity: '신격',
  creature: '괴수',
  artifact: '유물',
  organization: '조직',
  concept: '개념',
  motif: '모티프',
  other: '기타',
}

export function typeLabel(type: string): string {
  return TYPE_LABEL[type as EntityType] ?? type
}

// License "tone" drives badge color: positive (open), caution (unknown/limited),
// restricted (no commercial / closed).
export type LicenseTone = 'open' | 'caution' | 'restricted'

const OPEN_RE = /(cc0|public\s*domain|pdm|cc[\s-]?by(?![\s-]?(nc|nd))|mit|unlicense|gutenberg)/i

export function licenseTone(license?: License | null): LicenseTone {
  if (!license) return 'caution'
  const name = (license.name ?? '').trim()
  if (!name || /unknown/i.test(name)) return 'caution'
  if (license.commercial_ok === false) return 'restricted'
  if (/(nc|nd|all\s*rights|©|proprietary|restricted)/i.test(name)) return 'restricted'
  if (OPEN_RE.test(name) || license.commercial_ok === true) return 'open'
  return 'caution'
}

export function licenseLabel(license?: License | null): string {
  const name = (license?.name ?? '').trim()
  return name || '라이선스 미상'
}
