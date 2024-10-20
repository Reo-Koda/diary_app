# diary_app
## English version<br/>
This app was created to provide a simplified understanding of front-end and back-end communication using Django.<br/>
I used Supu's (http://www.youtube.com/@pythonvtuber9917) introduction to Django video as a reference in creating this app. (Video link: https://www.youtube.com/watch?v=r9QUdzVGHJU)<br/>
<br/>
Based on Supu's diary app, I decided to create a website like Qiita where various people can post and browse.<br/>
<br/>
Main Language<br/>
Python<br/>
Frameworks <br/>
Django<br/>
<br/>
### Reflections and Future Prospects<br/>
First, as mentioned above, I learned by writing my own program along with Sapoo's video, and then I wrote the program while racking my brains to add the login function. I wrote the program with a lot of trouble to add the login function.<br/>
The process of completing the login, logout, signup, etc. functions one after another was fun and engrossing.<br/>
However, I realized that the development environment and the production environment are completely different.<br/>
Countless times it worked in the development environment but not in the production environment.<br/>
I think we spent particular time on the issue of static files like CSS and JS not loading in the production environment.<br/>
I used a service called heroku to deploy this application, but the database called Heroku Postgres provided by that service could not display the images. If you want to display images in that database, it seems that you need to store the images as binary information in the database or use an external service like Amazon S3.<br/>
Looking back on this app, the good parts were: learning more efficient and versatile CSS techniques, learning how Django works and being able to write some Django programs, and being able to solve problems when I faced them. I felt like I gained the ability to solve problems when I faced them.<br/>
The bad part was the lack of planning that was exposed. We should have thought deeply about what functions to add before entering the development environment.<br/>
To sum up, this application was frankly like a social networking service. If I have a chance to make another application, I would like to add a comment function and make a SNS application.<br/>
I think I will make a new social networking application maybe tomorrow. The languages will be typescript and golang.<br/>
The reason is that we had built an app using React before building this app, and we gave up on that app because it was too large and would have taken years to build. It would have taken less than a week to make this app.<br/>
I would also like to learn Java from scratch, as I have never studied Java before.
<br/><br/>
## 日本語版<br/>
このアプリはDjangoを用いてフロントエンドとバックエンドの通信を簡易的に理解するために作成しました。<br/>
このアプリを作るにあたってサプーさん (http://www.youtube.com/@pythonvtuber9917) のDjango入門の動画を参考にさせていただいた。(動画リンク：https://www.youtube.com/watch?v=r9QUdzVGHJU)<br/>
<br/>
サプーさんの日記アプリをベースにQiitaのようにいろいろな人が投稿、閲覧できるようなサイトを目指すことにした。<br/>
<br/>
主な使用言語<br/>
Python<br/>
使用フレームワーク<br/>
Django<br/>
<br/>
### 振り返りおよび今後について<br/>
まず、前述のとおりサプーさんの動画に沿ってプログラムを自分で記述しながら学習をしたわけだが、そのあとにログイン機能をつけるにあたりかなり頭を悩ませながらプログラムを書いていった。初めて触るフレームワークであることも相まってネットの情報とChatGPTを頼りに機能を作っていった。<br/>
そうしてログイン機能ログアウト機能サインアップ機能などを次々と完成させていくその作業は楽しく夢中になった。<br/>
しかし開発環境と本番環境はまったく違うことを思い知った。<br/>
開発環境ではうまくいったのに本番環境ではうまくいかないが数えきれないくらい起きた。<br/>
CSSやJSのような静的ファイルが本番環境で読み込まれないという問題には特に時間を使ったと思う。<br/>
また、デプロイした後に追加したい機能を思いついた際、本番環境用のデータベースしかなく新たに開発していくやり方が分からず途方にくれた。とてもめんどくさい手順を踏めばできると思うが、開発環境のようなスピードで開発する方法ではない。<br/>
このアプリをデプロイするためにherokuというサービスを使用したが、そのサービスが提供するHeroku Postgresというデータベースでは画像を表示させることができなかった。そのデータベースの中で画像を表示させたい場合、画像をバイナリ情報にしてデータベースに収納する方法とAmazon S3のような外部のサービスを利用する必要があるようだ。<br/>
このアプリ制作を振り返り、よかったところは、CSSのより効率的で汎用性の高い技術を学習することができたこと。Djangoの仕組みを知り、多少なりともDjangoのプログラムを書けるようになったこと。トラブルに直面した時の解決する力が身についたように思えたこと。<br/>
悪かったところは計画性のなさが露呈したこと。開発環境に入る前の段階でどんな機能を付けるのかなどを深く考えておくべきだった。<br/>
総括として今回のアプリはぶっちゃけSNSみたいな感じになった。別のアプリを作る機会があったら、コメント機能を付け足してSNSアプリを作ってみたくなった。<br/>
もしかしたら明日にでも新たなSNSアプリをつくると思う。その時の使用言語はtypescriptとgolangになるであろう。<br/>
理由はこのアプリを作る前にReactを用いてアプリを作っていたからであり、そのアプリは規模が大きすぎて何年かかるかわからず断念してしまった。今回のアプリを作るのにかかった時間は一週間もないだろう。<br/>
いろいろなAPIにも触れてみたい。Javaを学んだことがないのでJavaをゼロから学んでみたい気持ちもある。
