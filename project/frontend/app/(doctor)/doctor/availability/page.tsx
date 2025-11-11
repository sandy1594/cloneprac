import { RoleLayout } from "@/components/RoleLayout";
import type { AvailabilitySlot } from "@/types";

function buildSampleSlots(): AvailabilitySlot[] {
  const today = new Date();
  const morningStart = new Date(today);
  morningStart.setHours(9, 0, 0, 0);
  const morningEnd = new Date(today);
  morningEnd.setHours(11, 0, 0, 0);
  const afternoonStart = new Date(today);
  afternoonStart.setHours(14, 0, 0, 0);
  const afternoonEnd = new Date(today);
  afternoonEnd.setHours(17, 0, 0, 0);

  return [
    {
      start_time: morningStart.toISOString(),
      end_time: morningEnd.toISOString(),
      is_available: true
    },
    {
      start_time: afternoonStart.toISOString(),
      end_time: afternoonEnd.toISOString(),
      is_available: true
    }
  ];
}

export default function DoctorAvailabilityPage() {
  const sampleSlots = buildSampleSlots();

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
      <h1>Availability</h1>
      <p className="muted">
        This view will sync with the `/api/doctor/availability` endpoint. Add a form to submit slots via `PUT` and
        optionally visualise using a calendar component (FullCalendar / React Big Calendar).
      </p>

      <section className="info-card" style={{ marginTop: "2rem" }}>
        <h2>Sample Slots</h2>
        <ul>
          {sampleSlots.map((slot, index) => (
            <li key={index}>
              {new Date(slot.start_time).toLocaleTimeString()} – {new Date(slot.end_time).toLocaleTimeString()} ·{" "}
              {slot.is_available ? "Available" : "Unavailable"}
            </li>
          ))}
        </ul>
      </section>
    </RoleLayout>
  );
}
