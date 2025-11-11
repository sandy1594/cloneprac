import { RoleLayout } from "@/components/RoleLayout";
import { getPendingDoctors } from "@/lib/api";
import type { DoctorProfile } from "@/types";

async function fetchPendingDoctors(): Promise<DoctorProfile[]> {
  try {
    return await getPendingDoctors();
  } catch {
    return [];
  }
}

export default async function AdminDoctorsPage() {
  const pendingDoctors = await fetchPendingDoctors();

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
      <h1>Doctor Verification</h1>
      <p className="muted">
        Approve practitioners via `/api/admin/doctors/:id/verify`. Add action buttons to trigger the API and refresh
        this list.
      </p>

      <table className="table">
        <thead>
          <tr>
            <th>Doctor</th>
            <th>Specialty</th>
            <th>Clinic</th>
            <th>Experience</th>
            <th>Fee</th>
          </tr>
        </thead>
        <tbody>
          {pendingDoctors.map((doctor) => (
            <tr key={doctor.id}>
              <td>{doctor.user?.name ?? `Doctor #${doctor.id}`}</td>
              <td>Specialty #{doctor.specialty_id}</td>
              <td>{doctor.clinic_name ?? "—"}</td>
              <td>{doctor.experience_years} yrs</td>
              <td>{doctor.fee ? `₹${doctor.fee}` : "—"}</td>
            </tr>
          ))}
          {pendingDoctors.length === 0 ? (
            <tr>
              <td colSpan={5}>No doctors awaiting verification right now.</td>
            </tr>
          ) : null}
        </tbody>
      </table>
    </RoleLayout>
  );
}
