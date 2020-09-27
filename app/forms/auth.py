from flask_login import current_user
from wtforms import Form,StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email,ValidationError,EqualTo,NumberRange
from app.models.user import User


class RegisterForm(Form):
    # nickname = StringField(validators=[DataRequired(),Length(2,10,message='昵称至少需要两个字符，最多不能超过十个')])
    nickname = StringField(validators=[DataRequired(),
                                       Length(2,10,message='昵称至少两个字符，最多不能超过10个字符')])
    email  = StringField(validators=[DataRequired(),Length(8,64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'),
                                         Length(6,32)])



   
    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')
class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64,message='电子邮箱长度必须在8个字符到12个字符'), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

class EmailForm(Form):
    email = StringField(validators=[DataRequired(),Length(5,64),
                                    Email(message='电子邮箱不符合规范')])
class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[DataRequired(),Length(6,32,message='密码长度至少需要6至32个字符之间'),
                                          EqualTo('password2',message='两次输入密码不相同')])
    password2 = PasswordField(validators=[DataRequired(),Length(6.32)])

class ChangePasswordForm(Form):
    old_password = PasswordField('原有密码', validators=[DataRequired()])
    new_password1 = PasswordField('新密码', validators=[
        DataRequired(), Length(6, 10, message='密码长度至少需要在6到20个字符之间'),
        EqualTo('new_password2', message='两次输入的密码不一致')])
    new_password2 = PasswordField('确认新密码字段', validators=[DataRequired()])

    def validate_old_password(self,field):
        user = User.query.filter_by(id=current_user.id).first()
        if not user.check_password(field.data):
            return ValidationError('原密码输入错误')



