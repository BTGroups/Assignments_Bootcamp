package main 

import (
	"fmt"
	"strings"
	"io/ioutil"
)


func main(){
	file , err := ioutil.ReadFile("sample.txt")
	if err != nil{
		fmt.Println("Failed to read the file")
	}

	str := string(file)
	str = strings.ReplaceAll(str, ",0,", ",FALSE,")
	str = strings.ReplaceAll(str, ",1,", ",TRUE,")

	 errr := ioutil.WriteFile("filefixedatgo.txt", []byte(str), 0644)
	 if errr != nil{
		fmt.Println("Failed to write the file")
}

	 fmt.Println("Treplacement done!")
}