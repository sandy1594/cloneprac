import { RoleLayout } from "@/components/RoleLayout";
import { MetricCard } from "@/components/MetricCard";
import { getDoctorList, getPatientAppointments } from "@/lib/api";
import type { Appointment, DoctorProfile } from "@/types";

async function fetchDoctors(): Promise<DoctorProfile[]> {
  try {
    return await getDoctorList();
  } catch {
    return [
      {
        id: 1,
        user_id: 101,
        specialty_id: 5,
        experience_years: 10,
        bio: "Cardiologist with a decade of experience in preventive care.",
        clinic_name: "City Heart Clinic",
        clinic_address: "Bangalore • MG Road",
        fee: 1200,
        rating: 4.8,
        verified: true,
        created_at: new Date().toISOString()
      }
    ];
  }
}

async function fetchAppointments(): Promise<Appointment[]> {
  try {
    return await getPatientAppointments();
  } catch {
    return [
      {
        id: 501,
        patient_id: 301,
        doctor_id: 1,
        scheduled_time: new Date(Date.now() + 86_400_000).toISOString(),
        status: "confirmed",
        reason: "Follow-up consultation"
      }
    ];
  }
}

export default async function PatientHomePage() {
  const [doctors, appointments] = await Promise.all([fetchDoctors(), fetchAppointments()]);

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
      <h1>Welcome back!</h1>
      <div className="card-grid">
        <MetricCard label="Upcoming visits" value={appointments.length} helper="Scheduled appointments" />
        <MetricCard label="Verified doctors" value={doctors.filter((doc) => doc.verified).length} helper="Trusted practitioners" />
      </div>

      <section>
        <h2>Highlighted Doctors</h2>
        <table className="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Specialty</th>
              <th>Clinic</th>
              <th>Fee</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {doctors.map((doctor) => (
              <tr key={doctor.id}>
                <td>{doctor.user?.name ?? `Doctor #${doctor.user_id}`}</td>
                <td>Specialty #{doctor.specialty_id}</td>
                <td>{doctor.clinic_name ?? "Not provided"}</td>
                <td>{doctor.fee ? `₹${doctor.fee}` : "—"}</td>
                <td>
                  <span className="pill">{doctor.verified ? "Verified" : "Pending"}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </RoleLayout>
  );
}
