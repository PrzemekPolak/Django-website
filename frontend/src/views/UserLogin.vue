<template>
  <div>
      <MenuTop        
            :user_name = user_name
            :logged_in_user = logged_in_user
             />
  </div>

<div class="userlog_container">
  <div>Logowanie (Przykładowy: login:Przemek/h:przemyslaw)</div>

  <form v-on:submit.prevent="submitForm" class="userlog_login_container">
    <div class="userlog_login_fields">
      <div class="userlog_login_text">
        <label class="userlog_login_el_txt" for="uname">Użytkownik:</label>
        <label class="userlog_login_el_txt" for="psw">Hasło:</label>
      </div>
      <div class="userlog_login_text">
        <input class="userlog_login_el_inp" type="text" v-model="form.uname">
        <input class="userlog_login_el_inp" type="password" v-model="form.psw">
      </div>
    </div>
        <button class="userlog_login_el_but" type="submit">Zaloguj się</button>
  </form>

    <div v-if="failed_login">Logowanie się nie powiodło</div>
</div>

</template>

<script>
import MenuTop from "@/components/MenuTop";

import axios from 'axios';

export default {
   name: "UserLogin",
   components: {
      MenuTop,
   },
   data() {
      return {
         list_data: [],
         logged_in_user: false,
         user_name: null,
         user_id: null,
         cash: null,
         failed_login: false,
         form: {
             uname: '',
             psw: '',
         }
      }
    },
  mounted() {
  },
  methods: {
    submitForm(){
        axios.post('http://127.0.0.1:8000/api/user_login/', this.form)
            .then((res) => {
                this.failed_login = res.data['failed_login']
                this.logged_in_user = res.data['logged']
                this.user_name = res.data['user']
                this.user_id = res.data['user_id']
                this.cash = res.data['cash']
                document.cookie = "logged_in_user=" + res.data['logged']
                document.cookie = "user_name=" + res.data['user']
                document.cookie = "user_id=" + res.data['user_id']
                document.cookie = "cash=" + res.data['cash']
            })
            .catch((error) => {
                console.log(error)
            })
        },

  },
  created() {
  }
};
</script>

<style>
body {
    font-size: 24px;
    color: white;
    background: rgb(79, 70, 70); 
}

.userlog_container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 50%;
}

.userlog_login_container {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    border: solid;
}

.userlog_login_fields {
    display: flex;
    align-items: center;
    padding: 10;
}

.userlog_login_text {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 10;
}

.userlog_login_el_txt {
    margin: 12;
}

.userlog_login_el_inp {
    margin: 10;
    border: solid red;
    padding: 5;
}

.userlog_login_el_but {    
    margin-bottom: 20;
    width: 120;
    height: 40;
    font-size: 20;
}

</style>