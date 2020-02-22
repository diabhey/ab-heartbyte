package main

import (
   "net/http"
   "fmt"
)

func HeartByte(w http.ResponseWriter, r *http.Request){
      fmt.Fprintf(w, "Welcome to HeartByte.io")
}

// Entrypoint into the App
func main(){
   http.HandleFunc("/", HeartByte)
   http.ListenAndServe(":8080", nil)
}

