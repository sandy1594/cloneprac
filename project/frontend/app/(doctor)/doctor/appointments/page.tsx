import { RoleLayout } from "@/components/RoleLayout";
import { getDoctorAppointments } from "@/lib/api";
import type { Appointment } from "@/types";

async function fetchAppointments(): Promise<Appointment[]> {
  try {
    return await getDoctorAppointments();
  } catch {
    return [];
  }
}

export default async function DoctorAppointmentsPage() {
  const appointments = await fetchAppointments();

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
      <h1>Appointments</h1>
      <p className="muted">Manage your daily schedule, patient queue, and visit status.</p>

      <table className="table">
        <thead>
          <tr>
            <th>Patient</th>
            <th>Time</th>
            <th>Status</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {appointments.map((appointment) => (
            <tr key={appointment.id}>
              <td>Patient #{appointment.patient_id}</td>
              <td>{new Date(appointment.scheduled_time).toLocaleTimeString()}</td>
              <td><span className="pill">{appointment.status}</span></td>
              <td>{appointment.reason ?? "—"}</td>
            </tr>
          ))}
          {appointments.length === 0 ? (
            <tr>
              <td colSpan={4}>No appointments on the calendar yet.</td>
            </tr>
          ) : null}
        </tbody>
      </table>
    </RoleLayout>
  );
}
