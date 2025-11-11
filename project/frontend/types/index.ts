export type UserRole = "patient" | "doctor" | "admin";

export type User = {
  id: number;
  name: string;
  email: string;
  phone?: string | null;
  role: UserRole;
  avatar_url?: string | null;
  created_at: string;
};

export type DoctorProfile = {
  id: number;
  user_id: number;
  specialty_id: number;
  experience_years: number;
  bio?: string | null;
  clinic_name?: string | null;
  clinic_address?: string | null;
  fee?: number | null;
  rating?: number | null;
  verified: boolean;
  created_at: string;
  user?: User;
};

export type AppointmentStatus = "pending" | "confirmed" | "completed" | "cancelled";

export type Appointment = {
  id: number;
  patient_id: number;
  doctor_id: number;
  scheduled_time: string;
  status: AppointmentStatus;
  reason?: string | null;
  doctor?: DoctorProfile;
};

export type AdminAnalytics = {
  users: { total: number };
  doctors: { total: number; pending_verification: number };
  appointments: { total: number; by_status: Record<AppointmentStatus, number> };
  payments: { total_revenue: number };
};

export type AvailabilitySlot = {
  start_time: string;
  end_time: string;
  is_available: boolean;
};
