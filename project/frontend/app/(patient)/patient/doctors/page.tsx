import { RoleLayout } from "@/components/RoleLayout";
import { getDoctorList } from "@/lib/api";
import type { DoctorProfile } from "@/types";

async function fetchDoctors(): Promise<DoctorProfile[]> {
  try {
    return await getDoctorList();
  } catch {
    return [];
  }
}

export default async function PatientDoctorsPage() {
  const doctors = await fetchDoctors();

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
      <h1>Doctor Directory</h1>
      <p className="muted">
        Filter by specialty, clinic location, or symptoms. (Filters are placeholders—wire them to `/api/doctors` query
        params when backend is live.)
      </p>

      <div className="card-grid" style={{ marginTop: "2rem" }}>
        {doctors.map((doctor) => (
          <article key={doctor.id} className="info-card">
            <h2>{doctor.user?.name ?? `Doctor #${doctor.id}`}</h2>
            <p className="muted">Specialty #{doctor.specialty_id} • {doctor.experience_years}+ years exp.</p>
            <p>{doctor.bio ?? "Bio coming soon."}</p>
            <p className="muted">{doctor.clinic_name ?? "Clinic TBD"} • {doctor.clinic_address ?? "Location TBD"}</p>
            <p className="pill">{doctor.fee ? `₹${doctor.fee}` : "Fee on request"}</p>
          </article>
        ))}
        {doctors.length === 0 ? <p>No doctors available yet.</p> : null}
      </div>
    </RoleLayout>
  );
}
