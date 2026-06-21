import type {
  ComposeOptions,
  ComposeResponse,
  FullTextResponse,
  SearchResponse,
  SourcesResponse,
  StoryEntity,
} from './types'

// Same-origin '/api' in dev (proxied by Vite) and in prod (served behind one host).
const BASE = import.meta.env.VITE_API_BASE ?? '/api'

async function getJSON<T>(path: string, signal?: AbortSignal): Promise<T> {
  const res = await fetch(`${BASE}${path}`, { signal })
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${await res.text().catch(() => res.statusText)}`)
  }
  return res.json() as Promise<T>
}

async function postJSON<T>(path: string, body: unknown, signal?: AbortSignal): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
    signal,
  })
  if (!res.ok) {
    let detail = res.statusText
    try {
      const data = await res.json()
      detail = data.detail ?? JSON.stringify(data)
    } catch {
      /* keep statusText */
    }
    throw new Error(`API ${res.status}: ${detail}`)
  }
  return res.json() as Promise<T>
}

export function search(
  q: string,
  opts: { sources?: string[]; limit?: number; signal?: AbortSignal } = {},
): Promise<SearchResponse> {
  const params = new URLSearchParams({ q })
  if (opts.sources?.length) params.set('sources', opts.sources.join(','))
  if (opts.limit) params.set('limit', String(opts.limit))
  return getJSON<SearchResponse>(`/search?${params.toString()}`, opts.signal)
}

export function listSources(signal?: AbortSignal): Promise<SourcesResponse> {
  return getJSON<SourcesResponse>('/sources', signal)
}

export function fetchFullText(id: string, signal?: AbortSignal): Promise<FullTextResponse> {
  return getJSON<FullTextResponse>(`/fulltext?id=${encodeURIComponent(id)}`, signal)
}

export function composeStatus(
  signal?: AbortSignal,
): Promise<{ available: boolean; model: string }> {
  return getJSON('/compose/status', signal)
}

export function compose(
  body: { brief: string; entities: StoryEntity[]; options: ComposeOptions },
  signal?: AbortSignal,
): Promise<ComposeResponse> {
  return postJSON<ComposeResponse>('/compose', body, signal)
}
