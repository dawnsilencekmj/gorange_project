import { apiClient } from '../../shared/api/client';

export const fetchKpi = async () => (await apiClient.get('/dashboard/kpi')).data;
export const fetchTimeseries = async () => (await apiClient.get('/dashboard/timeseries')).data;
