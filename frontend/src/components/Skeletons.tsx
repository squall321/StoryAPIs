// Loading placeholders that mirror the real layout so the page doesn't jump.

export function CardSkeleton() {
  return (
    <div className="card card-skeleton" aria-hidden>
      <div className="sk sk-cover" />
      <div className="card-body">
        <div className="sk sk-line sk-badge" />
        <div className="sk sk-line sk-title" />
        <div className="sk sk-line" />
        <div className="sk sk-line sk-short" />
        <div className="card-tags">
          <div className="sk sk-chip" />
          <div className="sk sk-chip" />
          <div className="sk sk-chip" />
        </div>
      </div>
    </div>
  )
}

export function ResultsSkeleton({ groups = 2, cards = 4 }: { groups?: number; cards?: number }) {
  return (
    <div className="results" aria-busy="true" aria-label="검색 중">
      {Array.from({ length: groups }).map((_, g) => (
        <section key={g} className="source-group">
          <div className="group-head">
            <div className="sk sk-line sk-grouptitle" />
          </div>
          <div className="cards">
            {Array.from({ length: cards }).map((_, c) => (
              <CardSkeleton key={c} />
            ))}
          </div>
        </section>
      ))}
    </div>
  )
}

export function TextSkeleton() {
  return (
    <div className="reader-skeleton" aria-busy="true" aria-label="전문 불러오는 중">
      {Array.from({ length: 8 }).map((_, i) => (
        <div key={i} className={`sk sk-line sk-text ${i % 4 === 3 ? 'sk-short' : ''}`} />
      ))}
    </div>
  )
}
