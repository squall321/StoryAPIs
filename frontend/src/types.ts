// Mirror of the backend's unified model (app/models/entities.py).

export interface License {
  name: string
  url?: string | null
  commercial_ok?: boolean | null
  attribution_required?: boolean | null
}

export interface Provenance {
  source_id: string
  source_name: string
  source_record_id?: string | null
  source_url?: string | null
  license: License
  language?: string | null
  retrieved_at: string
}

export interface TimeRef {
  label?: string | null
  start_year?: number | null
  end_year?: number | null
}

export interface MediaRef {
  type: string
  url: string
  thumbnail_url?: string | null
  caption?: string | null
}

export type EntityType =
  | 'person' | 'place' | 'event' | 'period' | 'work' | 'deity'
  | 'creature' | 'artifact' | 'organization' | 'concept' | 'motif' | 'other'

export interface StoryEntity {
  id: string
  type: EntityType
  title: string
  aliases: string[]
  summary?: string | null
  description?: string | null
  full_text?: string | null
  languages: string[]
  tags: string[]
  time?: TimeRef | null
  media: MediaRef[]
  provenance: Provenance
  extra: Record<string, unknown>
}

export interface SearchHit {
  entity: StoryEntity
  score?: number | null
  snippet?: string | null
}

export interface SourceResult {
  source_id: string
  source_name: string
  hits: SearchHit[]
  total?: number | null
  error?: string | null
  elapsed_ms?: number | null
}

export interface SearchResponse {
  query: string
  results: SourceResult[]
  total_hits: number
  elapsed_ms?: number | null
}

export interface SourceMeta {
  id: string
  name: string
  description: string
  homepage?: string | null
  regions: string[]
  languages: string[]
  entity_types: EntityType[]
  capabilities: string[]
  license: License
  auth_required: boolean
  enabled: boolean
  notes?: string | null
}
