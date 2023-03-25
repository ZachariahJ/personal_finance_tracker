<template>
  <div class="calender">
    <div class="month">
      <ul>
        <li class="prev">&#10094;</li>
        <li class="next">&#10095;</li>
        <li>
          March<br />
          <span>2023</span>
        </li>
      </ul>
    </div>
    <ul class="weekdays">
      <li>Mo</li>
      <li>Tu</li>
      <li>We</li>
      <li>Th</li>
      <li>Fr</li>
      <li>Sa</li>
      <li>Su</li>
    </ul>
    <ul class="days">
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
      <li>5</li>
      <li>6</li>
      <li>7</li>
      <li>8</li>
      <li>9</li>
      <li>10</li>
      <li>11</li>
      <li>12</li>
      <li>13</li>
      <li>14</li>
      <li>15</li>
      <li>16</li>
      <li>17</li>
      <li>18</li>
      <li>19</li>
      <li>20</li>
      <li>21</li>
      <li>22</li>
      <li>23</li>
      <li>24</li>
      <li>25</li>
      <li>26</li>
      <li>27</li>
      <li>28</li>
      <li>29</li>
      <li>30</li>
      <li>31</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from "vue";
</script>

<style lang="scss" scoped>
@import "../assets/css/vars.scss";
.calender {
  margin: 30px auto;
  background-color: $white;
  width: 90%;
  height: 80%;
  display: flex;
  flex-direction: column;

}

.month {
  padding: 70px 25px;
  width: 100%;
  background: #1abc9c;
  text-align: center;
}

.month ul {
  margin: 0;
  padding: 0;
}

.month ul li {
  color: white;
  font-size: 20px;
  text-transform: uppercase;
  letter-spacing: 3px;
}

.month .prev {
  float: left;
  padding-top: 10px;
}

.month .next {
  float: right;
  padding-top: 10px;
}

.weekdays {
  margin: 0;
  padding: 10px 0;
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #ddd;
}

.weekdays li {
  display: inline-block;
  width: 13.6%;
  color: #666;
  text-align: center;
  width: 13%;
}

.days {
  padding: 10px 0;
  background: #eee;
  margin: 0;
  height: 70px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: center;
  
}

.days li {
  list-style-type: none;
  display: inline-block;
  text-align: center;
  margin-bottom: 5px;
  font-size: 12px;
  color: #777;
  width: 13%;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.days li .active {
  padding: 5px;
  background: #1abc9c;
  color: white !important;
}
</style>
