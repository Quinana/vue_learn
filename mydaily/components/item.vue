<template>
    <a class="daily-item">
         <div class="daily-img" v-if="data.images">
             <img :src="imgPath + data.images[0]">
         </div>

         <div class="daily-title" :class="{noImg:!data.images}">{{data.title}}</div>
    </a>
</template>
<script>
import $ from '../libs/util';
export default{
    props:{
         data:{
             type:Object
         }
    },
    data(){
        return{
           imgPath:$.imgPath//imgPath是$对象的一个属性
        }
    }
}
//将item项分为有data.image(封面图)和无封面图(noImg)两类
</script>