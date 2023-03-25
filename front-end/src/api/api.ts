import axios from "axios";

const BASE_URL = "";

export interface Transaction {
  id: number;
  date: string;
  type: string;
  detail: string;
  amount: number;
}

export const getTally = async () => {
  const data = await axios("api/transactions");
  if (data.status === 200) {
    return data.data as Transaction[];
  } else {
    return [];
  }
};

export const addTally = async (sentence: string) => {
  const data = await axios.post("api/transactions", { sentence });
  if (data.status === 200) {
    return data.data as Transaction[];
  } else {
    return [] as Transaction[];
  }
};

export const totalMoney = async () => {
  const data = await axios.get("api/transactions/sum");
  if (data.status === 200) {
    return data.data as number;
  } else {
    return 0;
  }
};

export const deleteTally = async (id: number) => {
  const data = await axios.delete(`api/transactions/${id}`);
  if (data.status === 200) {
    return data.data as Transaction[];
  } else {
    return [] as Transaction[];
  }
};
