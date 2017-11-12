# DBDesigingTask
Database Designing Task. NO FURTHER UASGE!

Architecture:
Python+MySQL PyMySQL

Task Description:

<p>
<h1>内容：</h1></br>
  <h4>设计一所大学的学籍管理数据库系统</h4></br>
<h2>基本要求</h2></br>
1.设计学籍管理数据库，符合给定的语义（P3），并实现一定的功能需求（P4）</br>
2.使用一种DBMS，具体不限，推荐SQL Server</br>
3.最后一次课提交上机报告，上课前交齐</br>
选作要求</br>
 )开发前台应用程序对上述数据库进行访问，以一定的界面实现其功能</br>
 )使用一种应用开发软件，如PowerBuilder 、VC等，具体不限</br>
 )最后一次上机课验收程序，并提交主要代码</br>

数据库语义</br>
1.学校有若干专业，每个专业每年招若干个班，每个班有若干学生</br>
2.每个专业有自己的教学计划，规定了该专业相关课程的性质（必修或选修）以及授课学期；例如，数据库课程对计算机专业为必修、在大三上学期，但对数学专业可能为选修、在大三下学期，而中文专业可能不学这门课</br>
3.一位教师可以给多个班带课，但不能给一个班带多门课</br>
4.一门课程最多允许学生一次补考；学生达到如下条件之一的被开除：不及格必修课累计达15学分、或不及格选修课累计达20学分</br>
5.上述语义未涉及到的事项和细节，可自行做出合理假定</br>

功能需求</br>
1.建库时应录入一定数量的（不能过少）学生、教师、课程、成绩等基本信息</br>
2.录入一位学生，应包含学号、姓名、性别、出生年月、班级等信息</br>
3.按学号、姓名、专业三种方式查询学生基本信息</br>
4.录入一位学生一门课的成绩</br>
5.查询一位学生所修的课程、性质（必修或选修）、学期、学分及成绩；查询他的必修课平均成绩、所有课程平均成绩（平均成绩应按学分加权）</br>
6.查询一位学生被哪些教师教过课</br>
7.查询快要被开除的学生（距被开除差3学分之内）</br>

注意事项</br>
1.在数据库的设计过程中需要运用规范化理论（第六章），避免出现插入/删除异常、数据冗余等问题</br>
2.必须设定关系的完整性规则，如实体完整性（例如主码），参照完整性（设置外码），用户定义的完整性（例如性别只能为“男”或“女”）</br>
3.可以使用索引来加快查询的速度</br>
4.可以使用视图来简化系统的设计</br>
5.选作限定：应用程序的开发能够实现系统功能即可，不要把大量时间花费在美化界面和不必要的代码上</br>

按照数据库设计的基本步骤，书写上机报告：</br>
1.需求分析（系统数据和功能）</br>
2.概念结构设计（E-R图设计）</br>
3.逻辑结构设计（E-R图转换为关系模型）</br>
4.功能实现（选用哪种DBMS，如何用SQL语句实现各功能，查询结果示例）</br>
5.应用程序开发（选作限定，简要介绍）</br>
6.遇到的主要问题及解决方法</br>
7.总结</br>
</p>