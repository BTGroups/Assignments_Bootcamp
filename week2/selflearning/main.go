package main 

import "fmt"

type BankAccount struct{
	Balance int 
}

func (Bank BankAccount) showBalance(){
	fmt.Println("Bnk balance:", Bank.Balance)
}

func (Bank *BankAccount) Deposit(amount int) {
	if amount <= 0{
		fmt.Println("cannot deposit amount")
	}

	Bank.Balance = amount + Bank.Balance
} 

func( Bank *BankAccount) Withdraw(amount int){
	if amount > Bank.Balance{
		fmt.Println("Amount is more to withdraw")
	}
	if amount < 0{
		fmt.Println("amount cannoy be accpeted")
	}

	Bank.Balance -= amount
}

