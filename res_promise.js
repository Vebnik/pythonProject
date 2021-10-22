 async function get_history (channel) {
        let get_history_url = 'url
        let get_history_form = new FormData();

        get_history_form.append(`limit`, `1`);
        get_history_form.append(`channel`, `${channel}`);
        get_history_form.append(`token`, `tokken`)

        let param_requests = {
            method: "POST",
            body: get_history_form,
            referrer: "about:client",
            credentials: "include",
        };

        response = await fetch(`${get_history_url}`, param_requests)
        if (response.ok){
            res_his = await response.json()
        }else {
            console.log(response.status)
        }
        last_thread_ts = res_his
        // Возвращает распарсеный промис объект, вернее его тело в виде jspn 
        return last_thread_ts

    }
