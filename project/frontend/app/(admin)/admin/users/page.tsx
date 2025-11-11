import { RoleLayout } from "@/components/RoleLayout";

const sampleUsers = [
  { id: 1, name: "Jane Doe", role: "patient", email: "jane@example.com" },
  { id: 2, name: "Dr. Arjun Mehta", role: "doctor", email: "arjun@example.com" },
  { id: 3, name: "Aisha Khan", role: "admin", email: "aisha@example.com" }
] as const;

export default function AdminUsersPage() {
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
      <h1>User Directory</h1>
      <p className="muted">
        Connect this view to `/api/admin/users` when implemented. Provide search, filters, and pagination.
      </p>

      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          {sampleUsers.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td><span className="pill">{user.role}</span></td>
            </tr>
          ))}
        </tbody>
      </table>
    </RoleLayout>
  );
}
