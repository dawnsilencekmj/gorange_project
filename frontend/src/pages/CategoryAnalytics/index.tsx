import { useEffect, useState } from 'react';
import { apiClient } from '../../shared/api/client';

export default function CategoryAnalyticsPage() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => {
    apiClient.get('/categories/stats').then((r) => setItems(r.data.items || []));
  }, []);
  return <div><h2>Category Analytics</h2><pre>{JSON.stringify(items, null, 2)}</pre></div>;
}
