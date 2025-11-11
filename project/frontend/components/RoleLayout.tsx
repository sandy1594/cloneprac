import Link from "next/link";
import type { ReactNode } from "react";

export type NavItem = {
  label: string;
  href: string;
};

type RoleLayoutProps = {
  title: string;
  navItems: NavItem[];
  children: ReactNode;
};

export function RoleLayout({ title, navItems, children }: RoleLayoutProps) {
  return (
    <div className="layout">
      <aside className="sidebar">
        <span className="sidebar__title">{title}</span>
        <nav>
          {navItems.map((item) => (
            <Link key={item.href} href={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <section className="content">{children}</section>
    </div>
  );
}
