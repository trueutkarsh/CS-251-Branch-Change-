from django.db import models

# Create your models here.
#student wil be entered through forms



#programs have to be entered manually
class program(models.Model):
    #programchoices=(('BT-CSE','BTech-Computer Science'),('DD-ELE','DUALDEGREE-ELECTRICAL'))
    name=models.CharField(max_length=30)
    sancstrength=models.IntegerField(default=0)
    currstrength=models.IntegerField(default=0)

    #this has to be done by us manuallymi

    def __unicode__(self):
        return self.name

    def __init__(self,*args, **kwargs):
     super(program,self).__init__(*args, **kwargs)
    '''
    def __init__(self,name,*args, **kwargs):
        super(models.Model,self).__init__(*args, **kwargs)
        self.name=name
    '''


class student(models.Model):

    CATGCHOICES=(('GE','GENERAL'),('SC','SCHEDULE CASTE'),('ST','SCHEDULE TRIBES'),('OB','OTHER BACKWARD CLASSES'))
    name=models.CharField(max_length=40,blank=False)
    rollno=models.CharField(max_length=9,blank=False)
    cpi=models.FloatField()
    currentbranch=models.ForeignKey(program,related_name='user')
    category=models.CharField(max_length=2,choices=CATGCHOICES)
    branchops=models.ManyToManyField(program,related_name='usr')


    def __unicode__(self):
        return self.name

    def __init__(self,*args, **kwargs):
         super(student,self).__init__(*args, **kwargs)
    '''
    def __init__(self,name,rollno,cpi,currentbranch,category,branchops,*args, **kwargs):
        super(models.Model,self).__init__(*args, **kwargs)
        self.name=name
        self.rollno=rollno
        self.cpi=cpi
        self.category=category
        self.currentbranch=program.objects.all().get(name=currentbranch)
        for x in branchops:
            self.branchops.add(program.objects.all().get(name=x))
    '''






