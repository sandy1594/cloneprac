import axios from "axios";

const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api",
  timeout: 8000
});

export async function getDoctorList() {
  const response = await apiClient.get("/doctors");
  return response.data;
}

export async function getPatientAppointments() {
  const response = await apiClient.get("/appointments");
  return response.data;
}

export async function getDoctorAppointments() {
  const response = await apiClient.get("/doctor/appointments");
  return response.data;
}

export async function getAdminAnalytics() {
  const response = await apiClient.get("/admin/analytics");
  return response.data;
}

export async function getPendingDoctors() {
  const response = await apiClient.get("/admin/doctors/pending-verification");
  return response.data;
}
