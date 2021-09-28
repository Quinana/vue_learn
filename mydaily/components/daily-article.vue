<template>
<div class="daily-article">
<div class="daily-article-title">{{data.title}}</div>
<div class="daily-article-content" v-html="data.body"></div>
</div>
</template>
<script>
import $ from '../libs/util'
export default{
    props:{
          id:{
              type:Number,
              default:0
          }
    },
    data:function(){
        return{
               data:{}
        } 
    },
    methods:{
           getArticle:function(){
                $.ajax.get('news/'+this.id).then(function(res){
                    
                })
           }
    },
    watch:{
        id(val){
            if(val){
                this.id.getArticle();
            }
        }
    }
}
</script>
