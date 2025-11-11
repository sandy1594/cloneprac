import { RoleLayout } from "@/components/RoleLayout";

const reportItems = [
  { title: "Monthly Revenue", description: "Exports transaction totals for finance reconciliation." },
  { title: "Appointment Trends", description: "Shows confirmed vs cancelled visits over time." },
  { title: "Doctor Performance", description: "Track average ratings, appointment volume, and queue times." }
] as const;

export default function AdminReportsPage() {
  return (
    <RoleLayout
      title="Admin Console"
      navItems={[
        { label: "Dashboard", href: "/admin/dashboard" },
        { label: "Doctor Verification", href: "/admin/doctors" },
        { label: "Users", href: "/admin/users" },
        { label: "Reports", href: "/admin/reports" }
      ]}
    >
      <h1>Reports & Analytics</h1>
      <p className="muted">
        Connect to `/api/admin/analytics` and extend with CSV / PDF exports. Consider embedding BI dashboards for deeper
        insights.
      </p>

      <div className="card-grid" style={{ marginTop: "2rem" }}>
        {reportItems.map((report) => (
          <article key={report.title} className="info-card">
            <h2>{report.title}</h2>
            <p>{report.description}</p>
            <p className="muted">Coming soon</p>
          </article>
        ))}
      </div>
    </RoleLayout>
  );
}
