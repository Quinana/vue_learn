<template>
<div class="daily">
    <div class="daily-nav">
        <a href="http://daily.zhihu.com/"><img class="logo" src="./images/logo.png"></a>
        <div class="daily-nav-item" :class="{on: type === 'recommend'}" @click="handleToRecommend">
            <span>每日推荐</span>
        </div>
    </div>
    <div id="dailylist" class="daily-list" ref="list">
             <div v-for="(list,index) in recommendList" :key="index">
                  <div class="daily-date">{{formatDay(list.date)}}</div>
                  <Item  @click.native="handleClick(item.id)" v-for="item in list.stories" :data="item" :key="item.id"></Item>
             </div>
    </div>
    <daily-article :id="articleId"></daily-article>
</div>
</template>
<script>
    import Item from './components/item.vue';
    import dailyArticle from './components/daily-article.vue';
    import $ from './libs/util';

export default{
  components: { Item,dailyArticle },
    data(){
        return{
            type:'recommend',
            recommendList:[],
            dailyTime:$.getTodayTime(),
            isLoading:false,
            list:[],
            articleId:0
        }
    },
    methods:{
        handleToRecommend:function(){
            this.type = 'recommend';
            this.recommendList = [];
            this.dailyTime = $.getTodayTime();
            this.getRecommendList(); 
        },
        getRecommendList:function(){
             this.isLoading = true;
             const prevDay = $.prevDay(this.dailyTime+86400000);//？为什么是+86400000(api接口如此设计,news/before/20210927,就是包含当天20210926的日报)
             $.ajax.get('news/before/'+prevDay).then(res =>{
                 this.recommendList.push(res);
                 this.isLoading = false;
             })
        },
        formatDay:function(date){
            var month = date.substr(4,2);
            var day =date.substr(6,2);
            return `${month} 月 ${day} 日`;  //需要注意的表达方式
        },
        handleClick:function(id){
            this.articleId = id;
            console.log(id);
        }
    },
    mounted(){
        this.getRecommendList();
        const $list = this.$refs.list;//通过this.$refs方法访问子组件信息
        $list.addEventListener('scroll',function(){
            if(this.isLoading)return;
            //已经滚动的距离+页面高度大于整个内容区域的高度时
           // if($list.scrollTop+document.body.clientHeight>=$list.scrollHeight){
               if($list.scrollTop+document.body.clientHeight>=$list.scrollHeight){
                 this.dailyTime -= 86400000;
                 this.getRecommendList();
            }
        })
    }
}
</script>