type MetricCardProps = {
  label: string;
  value: string | number;
  helper?: string;
};

export function MetricCard({ label, value, helper }: MetricCardProps) {
  return (
    <div className="info-card">
      <h2>{label}</h2>
      <p className="pill">{value}</p>
      {helper ? <p className="muted">{helper}</p> : null}
    </div>
  );
}
