import { RoleLayout } from "@/components/RoleLayout";
import { MetricCard } from "@/components/MetricCard";
import { getDoctorAppointments } from "@/lib/api";
import type { Appointment } from "@/types";

async function fetchAppointments(): Promise<Appointment[]> {
  try {
    return await getDoctorAppointments();
  } catch {
    return [];
  }
}

export default async function DoctorDashboardPage() {
  const appointments = await fetchAppointments();
  const upcoming = appointments.filter((appt) => new Date(appt.scheduled_time) > new Date());

  return (
    <RoleLayout
      title="Doctor Workspace"
      navItems={[
        { label: "Dashboard", href: "/doctor/dashboard" },
        { label: "Appointments", href: "/doctor/appointments" },
        { label: "Availability", href: "/doctor/availability" },
        { label: "Profile", href: "/doctor/profile" }
      ]}
    >
      <h1>Today&apos;s Snapshot</h1>
      <div className="card-grid">
        <MetricCard label="Upcoming" value={upcoming.length} helper="Appointments ahead" />
        <MetricCard label="Total today" value={appointments.length} helper="All scheduled visits" />
      </div>

      <section>
        <h2>Queue overview</h2>
        <table className="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Time</th>
              <th>Status</th>
              <th>Reason</th>
            </tr>
          </thead>
          <tbody>
            {appointments.slice(0, 5).map((appointment) => (
              <tr key={appointment.id}>
                <td>{appointment.id}</td>
                <td>{new Date(appointment.scheduled_time).toLocaleString()}</td>
                <td><span className="pill">{appointment.status}</span></td>
                <td>{appointment.reason ?? "—"}</td>
              </tr>
            ))}
            {appointments.length === 0 ? (
              <tr>
                <td colSpan={4}>No appointments scheduled yet.</td>
              </tr>
            ) : null}
          </tbody>
        </table>
      </section>
    </RoleLayout>
  );
}
