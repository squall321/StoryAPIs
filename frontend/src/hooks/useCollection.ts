import { useCallback, useEffect, useState } from 'react'
import type { StoryEntity } from '../types'

const KEY = 'storyapis.collection.v1'

function load(): StoryEntity[] {
  try {
    const raw = localStorage.getItem(KEY)
    return raw ? (JSON.parse(raw) as StoryEntity[]) : []
  } catch {
    return []
  }
}

// A localStorage-backed "수집함" of source material the writer is gathering.
export function useCollection() {
  const [items, setItems] = useState<StoryEntity[]>(() => load())

  useEffect(() => {
    try {
      localStorage.setItem(KEY, JSON.stringify(items))
    } catch {
      /* ignore quota errors */
    }
  }, [items])

  const has = useCallback((id: string) => items.some((e) => e.id === id), [items])

  const toggle = useCallback(
    (entity: StoryEntity) =>
      setItems((prev) =>
        prev.some((e) => e.id === entity.id)
          ? prev.filter((e) => e.id !== entity.id)
          : [...prev, entity],
      ),
    [],
  )

  const remove = useCallback(
    (id: string) => setItems((prev) => prev.filter((e) => e.id !== id)),
    [],
  )

  const clear = useCallback(() => setItems([]), [])

  return { items, has, toggle, remove, clear, count: items.length }
}

export type Collection = ReturnType<typeof useCollection>
