import { RoleLayout } from "@/components/RoleLayout";
import { getPatientAppointments } from "@/lib/api";
import type { Appointment } from "@/types";

async function fetchAppointments(): Promise<Appointment[]> {
  try {
    return await getPatientAppointments();
  } catch {
    return [];
  }
}

export default async function PatientAppointmentsPage() {
  const appointments = await fetchAppointments();

  return (
    <RoleLayout
      title="Patient Workspace"
      navItems={[
        { label: "Home", href: "/patient" },
        { label: "Doctor Directory", href: "/patient/doctors" },
        { label: "Appointments", href: "/patient/appointments" },
        { label: "Profile", href: "/patient/profile" }
      ]}
    >
      <h1>My Appointments</h1>
      <p className="muted">Status updates sync with the `/api/appointments` endpoint.</p>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Doctor</th>
            <th>Scheduled</th>
            <th>Status</th>
            <th>Reason</th>
          </tr>
        </thead>
        <tbody>
          {appointments.map((appointment) => (
            <tr key={appointment.id}>
              <td>{appointment.id}</td>
              <td>{appointment.doctor?.user?.name ?? `Doctor #${appointment.doctor_id}`}</td>
              <td>{new Date(appointment.scheduled_time).toLocaleString()}</td>
              <td><span className="pill">{appointment.status}</span></td>
              <td>{appointment.reason ?? "—"}</td>
            </tr>
          ))}
          {appointments.length === 0 ? (
            <tr>
              <td colSpan={5}>No appointments yet. Book your first one!</td>
            </tr>
          ) : null}
        </tbody>
      </table>
    </RoleLayout>
  );
}
