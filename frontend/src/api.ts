import type { FullTextResponse, SearchResponse, SourcesResponse } from './types'

// Same-origin '/api' in dev (proxied by Vite) and in prod (served behind one host).
const BASE = import.meta.env.VITE_API_BASE ?? '/api'

async function getJSON<T>(path: string, signal?: AbortSignal): Promise<T> {
  const res = await fetch(`${BASE}${path}`, { signal })
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${await res.text().catch(() => res.statusText)}`)
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
