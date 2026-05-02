import { useEffect, useState } from 'react';
import { fetchKpi, fetchTimeseries } from '../../features/dashboard/api';

export default function HomePage() {
  const [kpi, setKpi] = useState<any>();
  const [series, setSeries] = useState<any[]>([]);

  useEffect(() => {
    fetchKpi().then(setKpi);
    fetchTimeseries().then((d) => setSeries(d.items || []));
  }, []);

  return (
    <div>
      <h2>Home Dashboard</h2>
      <pre>{JSON.stringify(kpi, null, 2)}</pre>
      <h3>Timeseries (avg close by date)</h3>
      <ul>
        {series.map((row) => (
          <li key={row.date}>{row.date}: {row.close}</li>
        ))}
      </ul>
    </div>
  );
}
