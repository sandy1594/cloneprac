import { RoleLayout } from "@/components/RoleLayout";
import { MetricCard } from "@/components/MetricCard";
import { getAdminAnalytics } from "@/lib/api";
import type { AdminAnalytics } from "@/types";

async function fetchAnalytics(): Promise<AdminAnalytics> {
  try {
    return await getAdminAnalytics();
  } catch {
    return {
      users: { total: 0 },
      doctors: { total: 0, pending_verification: 0 },
      appointments: { total: 0, by_status: { pending: 0, confirmed: 0, completed: 0, cancelled: 0 } },
      payments: { total_revenue: 0 }
    };
  }
}

export default async function AdminDashboardPage() {
  const analytics = await fetchAnalytics();

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
      <h1>Platform Overview</h1>
      <div className="card-grid">
        <MetricCard label="Users" value={analytics.users.total} helper="Patients + Doctors + Admins" />
        <MetricCard label="Doctors" value={analytics.doctors.total} helper="Total onboarded" />
        <MetricCard label="Pending Verification" value={analytics.doctors.pending_verification} />
        <MetricCard label="Revenue" value={`₹${analytics.payments.total_revenue.toLocaleString()}`} />
      </div>

      <section>
        <h2>Appointments By Status</h2>
        <table className="table">
          <thead>
            <tr>
              <th>Status</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(analytics.appointments.by_status).map(([status, count]) => (
              <tr key={status}>
                <td>{status}</td>
                <td>{count}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </RoleLayout>
  );
}
