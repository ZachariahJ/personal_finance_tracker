<template>
  <div class="top">
    <div class="card balance">
      <h2>Total Balance</h2>
      <h1 class="green">${{ tally.balance }}</h1>
    </div>
    <div class="inc-exp">
      <div class="card income">
        <h4>Monthly Income</h4>
        <h3 class="green">${{ tally.income }}</h3>
      </div>
      <div class="card expense">
        <h4>Monthly Expense</h4>
        <h3 class="red">${{ tally.expense }}</h3>
      </div>
    </div>
  </div>
  <div class="table" id="table">
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Amount</th>
          <th>Type</th>
          <th>Detail</th>
          <th>Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in tally.data" :key="item.id">
          <td>{{ item.date }}</td>
          <td>
            <div class="triangle" :class="item.amount >= 0 ? '' : 'down'"></div>
            {{ item.amount }}
          </td>
          <td>{{ item.type }}</td>
          <td>{{ item.detail }}</td>
          <td><button @click="deleteBtn(item.id)">Delete</button></td>
        </tr>
      </tbody>
    </table>
  </div>
  <Recorder width="90%" :tally="tally" />
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import Recorder from "../components/Recorder.vue";
import { getTally, Transaction, totalMoney, deleteTally } from "../api/api";

let tally = reactive<{ data: Transaction[]; balance: number; income: number; expense: number }>({
  data: [],
  balance: 0,
  income: 0,
  expense: 0,
});
onMounted(async () => {
  tally.data = await getTally();
  update();
  setInterval(async () => {
    tally.data = await getTally();
    update();
  }, 1000);
});

const update = async () => {
  tally.income = 0;
  tally.expense = 0;
  for (const item of tally.data) {
    if (item.amount >= 0) {
      tally.income += item.amount;
    } else {
      tally.expense -= item.amount;
    }
  }
  tally.balance = await totalMoney();
};

const deleteBtn = async (id: number) => {
  tally.data = await deleteTally(id);
  update();
};
</script>

<style lang="scss" scoped>
@import "@/assets/css/vars.scss";

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px auto;
  border-radius: 20px;
  width: 90%;

  .card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 200px;
    height: 150px;
    background-color: $color-primary;
    border-radius: 20px;
    color: $white;
  }

  .balance {
    width: 30%;
    height: 150px;
  }

  .inc-exp {
    display: flex;
    flex-direction: column;
    align-items: end;
    justify-content: space-between;
    width: 60%;
    height: 150px;

    .income {
      width: 50%;
      margin-bottom: 10px;
    }

    .expense {
      width: 50%;
    }
  }
}

.table {
  height: calc(100vh - 300px);
  overflow-y: auto;
  margin: 0 auto;
  width: 90%;
}

table {
  border-collapse: collapse;
  width: 100%;
}

.triangle {
  display: inline-block;
  width: 0;
  height: 0;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-bottom: 14px solid $green;
}

.down {
  border-bottom: none;
  border-top: 14px solid $red;
}

th,
td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid $color-primary;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #e6e6e6;
}

tr:hover {
  background-color: #f5f5f5;
}
</style>
