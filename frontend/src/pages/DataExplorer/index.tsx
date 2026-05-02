import { useEffect, useState } from 'react';
import { apiClient } from '../../shared/api/client';

export default function DataExplorerPage() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => {
    apiClient.get('/explorer/rows?limit=20').then((r) => setItems(r.data.items || []));
  }, []);
  return <div><h2>Data Explorer</h2><pre>{JSON.stringify(items, null, 2)}</pre></div>;
}
