import { RoleLayout } from "@/components/RoleLayout";

export default function DoctorProfilePage() {
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
      <h1>Profile</h1>
      <p className="muted">
        This section will integrate with `/api/doctor/profile` to update biography, clinic info, and fees. Implement a
        form and form-state management (React Hook Form) to persist data.
      </p>

      <section className="info-card" style={{ marginTop: "2rem" }}>
        <h2>Current Profile</h2>
        <ul>
          <li>Name: Dr. Arjun Mehta</li>
          <li>Specialty: Cardiology</li>
          <li>Clinic: City Heart Clinic</li>
          <li>Consultation fee: ₹1200</li>
        </ul>
      </section>
    </RoleLayout>
  );
}
