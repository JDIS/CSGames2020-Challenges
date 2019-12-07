from flask import Flask
from checker import *
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.0"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.19.0/axios.min.js" integrity="sha256-S1J4GVHHDMiirir9qsXWc8ZWw74PHHafpsHp5PXtjTs=" crossorigin="anonymous"></script>
<div id="app">
    Backend URL: <input v-model="backend" /><br>
    <input type="radio" v-model="lvl" value="0"> LVL0<br>
    <input type="radio" v-model="lvl" value="1"> LVL1<br>
    <input type="radio" v-model="lvl" value="2"> LVL2<br>
    <input type="radio" v-model="lvl" value="3"> LVL3<br>
    <button @click="submit()">Go</button><br>
    <div v-if="inprogress" >Requête en cours....</div>
    <div v-if="reponse">Réponse du serveur de correction:</div><br>
    <div v-html="reponse"></div>
</div>
<script>
let vm = new Vue({
    el: '#app',
    data() {
        return {
            lvl: 0,
            backend: "",
            reponse: "",
            inprogress: false
        }
    },
    methods: {
        submit() {
            this.reponse = ""
            this.inprogress = true
            axios.get(`/check/${this.lvl}?backend=${this.backend}`).then((response) => {
                this.reponse = response.data
                this.inprogress = false
            }).catch((error) => {
                this.reponse = error.response.data
                this.inprogress = false
            })
        }
    }
})
</script>
"""

@app.route("/check/0")
def check0():
    if testlvl0(request.args.get('backend')):
        return os.environ.get('lvl0')

@app.route("/check/1")
def check1():
    if testlvl1(request.args.get('backend')):
        return os.environ.get('lvl1')

@app.route("/check/2")
def check2():
    if testlvl2(request.args.get('backend')):
        return os.environ.get('lvl2')

@app.route("/check/3")
def check3():
    if testlvl3(request.args.get('backend')):
        return os.environ.get('lvl3')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)