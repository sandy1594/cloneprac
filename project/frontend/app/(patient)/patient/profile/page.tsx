import { RoleLayout } from "@/components/RoleLayout";

export default function PatientProfilePage() {
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
      <h1>Profile</h1>
      <p className="muted">
        Profile editing connects to `/api/auth/verify` to fetch user details and future `/api/profile` endpoints for
        updates. Add forms and validation hooks once backend auth is wired.
      </p>

      <section className="info-card" style={{ marginTop: "2rem" }}>
        <h2>Account Overview</h2>
        <ul>
          <li>Name: Jane Doe</li>
          <li>Email: jane@example.com</li>
          <li>Phone: +91 90000 00000</li>
        </ul>
      </section>
    </RoleLayout>
  );
}
