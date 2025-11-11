import Link from "next/link";

export default function HomePage() {
  return (
    <main className="landing">
      <section className="landing__hero">
        <h1>Healthcare Platform</h1>
        <p>
          End-to-end appointment scheduling, doctor management, and admin controls for modern clinics.
        </p>
      </section>

      <section className="landing__grid">
        <LandingCard
          title="Patient Portal"
          description="Search doctors, book appointments, manage health records."
          href="/patient"
        />
        <LandingCard
          title="Doctor Workspace"
          description="Manage schedules, patient queues, and clinical insights."
          href="/doctor/dashboard"
        />
        <LandingCard
          title="Admin Console"
          description="Verify practitioners, monitor analytics, reconcile payments."
          href="/admin/dashboard"
        />
      </section>
    </main>
  );
}

type LandingCardProps = {
  title: string;
  description: string;
  href: string;
};

function LandingCard({ title, description, href }: LandingCardProps) {
  return (
    <Link href={href} className="landing-card">
      <h2>{title}</h2>
      <p>{description}</p>
      <span className="landing-card__cta">Explore →</span>
    </Link>
  );
}
