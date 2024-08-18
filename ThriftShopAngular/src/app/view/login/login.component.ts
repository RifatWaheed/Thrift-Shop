import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MessageService } from 'primeng/api';
import { ToastModule } from 'primeng/toast';


class UserDB {
  email: string;
  password: string;
  confirmPassword?: string;
}
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, ToastModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
  providers: [MessageService]
})
export class LoginComponent {
  loginTitle: string = "Login";
  userStateText: string = "New user? ";
  toggleTitle: string = "Sign up";
  isSignupClicked: boolean = false;

  passwordTextType: string = "password";
  confirmPasswordTextType: string = "password";
  isPasswordVisible: boolean = false;
  isConfirmPasswordVisible: boolean = false;

  isPasswordFocus: boolean = false;
  email: string = '';
  password: string = '';
  confirmPassword: string = '';
  hintText: string = "Required 1 uppercase, 1 digit and 8 characters min";

  users: UserDB[] = [];

  constructor(
    private messageService: MessageService,

  ) {
  }

  onSignupClicked() {
    if (!this.isSignupClicked) {
      this.isSignupClicked = true;
      this.isPasswordVisible = false;
      this.passwordTextType = "password";
      this.loginTitle = "Sign up";
      this.userStateText = "Existing user? ";
      this.toggleTitle = "Login";
    }
    else {
      this.isSignupClicked = false;
      this.isPasswordVisible = false;
      this.passwordTextType = "password"
      this.isConfirmPasswordVisible = false;
      this.loginTitle = "Login";
      this.userStateText = "New user? ";
      this.toggleTitle = "Sign up";
    }
    this.password = '';
    this.confirmPassword = '';
  }

  onShowPasswordClicked() {
    this.isPasswordVisible = true;
    this.passwordTextType = "text";
  }
  onHidePasswordClicked() {
    this.isPasswordVisible = false;
    this.passwordTextType = "password";
  }

  onShowConfirmPasswordClicked() {
    this.isConfirmPasswordVisible = true;
    this.confirmPasswordTextType = "text";
  }
  onHideConfirmPasswordClicked() {
    this.isConfirmPasswordVisible = false;
    this.confirmPasswordTextType = "password";
  }

  onPasswordFocus() {
    this.isPasswordFocus = true;
  }
  onPasswordBlur() {
    this.isPasswordFocus = false;
  }

  validate(user: UserDB): boolean {
    let hasAtTheRate = false;
    let emailValid = false;

    let hasUppercase = false;
    let hasDigit = false;

    if (!user.email) {
      this.messageService.add({
        key: 'tc',
        life: 1000,
        severity: 'warn',
        summary: 'Invalid E-mail',
        detail: 'Please enter an e-mail',
      });
      return false;
    }

    if (!user.password) {
      this.messageService.add({
        key: 'tc',
        life: 1000,
        severity: 'warn',
        summary: 'Invalid Password',
        detail: 'Please enter a password',
      });
      return false;
    }

    if (!user.confirmPassword) {
      this.messageService.add({
        key: 'tc',
        life: 1000,
        severity: 'warn',
        summary: 'Confirm Password Empty',
        detail: "Confirm Password can't be empty",
      });
      return false;
    }

    // for(let i =0; i<user.email.length; i++){
    //   if(user.email[i] === '@' ){
    //     hasAtTheRate = true;
    //     break;
    //   }
    // }

    // if(!hasAtTheRate){
    //   this.messageService.add({
    //     key: 'tc',
    //     life: 1000,
    //     severity: 'Error',
    //     summary: 'Invalid Email',
    //     detail: "Please Enter a valid Email",
    //   });
    //   return false;
    // }


    for (let i = 0; i < user.email.length; i++) {
      if (user.email.charAt(i) === "@") {
        hasAtTheRate = true;
      }
    }
    if (hasAtTheRate) {
      const emailParts = user.email.split('@');
      const emailDomain = emailParts.length === 2 ? emailParts[1] : '';
      emailValid = emailDomain === 'gmail.com' || emailDomain === 'yahoo.com';
    }
    else {
      this.messageService.add({
        key: 'tc',
        life: 1000,
        severity: 'error',
        summary: 'Invalid Email',
        detail: "Please Enter a valid Email",
      });
      return false;
    }

    for (let i = 0; i < user.password.length; i++) {
      if (user.password.charAt(i) >= "A" && user.password.charAt(i) <= "Z") {
        hasUppercase = true;
      }
      else if (user.password.charAt(i) >= "0" && user.password.charAt(i) <= "9") {
        hasDigit = true;
      }
      else {
        hasUppercase = false;
        hasDigit = false;
      }
    }
    const passwordLength = user.password.length >= 8 && user.password.length <= 16;
    const passwordValid = passwordLength && hasUppercase && hasDigit;

    const passwordMatch = user.password === user.confirmPassword;

    // Combine all conditions
    const allConditionsValid = emailValid && passwordValid && passwordMatch;

    if (!emailValid) {
      //Email Invalid
    }
    if (!passwordValid) {
      //Password Invalid
    }
    if (!passwordMatch) {
      //Password & confirm password mismatch
    }

    return allConditionsValid
  }

  onSubmit() {
    if (this.loginTitle === "Sign up") {
      const newUser = new UserDB();
      newUser.email = this.email;
      newUser.password = this.password;
      newUser.confirmPassword = this.confirmPassword;
      if (this.validate(newUser)) {
        // this.users.push(newUser);
      }
      else {
        console.log("Feild are blank")
      }
    }
  }

}
