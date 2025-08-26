<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>To-Do List</title>
<style>
  body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
  .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 8px; }
  h2 { text-align: center; }
  input[type="text"] { width: 75%; padding: 10px; }
  button { padding: 10px 15px; }
  ul { list-style: none; padding: 0; }
  li { background: #eee; margin: 5px 0; padding: 10px; border-radius: 4px; cursor: pointer; }
  li.completed { text-decoration: line-through; color: gray; }
</style>
</head>
<body>
  <div class="container">
    <h2>My To-Do List</h2>
    <form id="todoForm">
      <input type="text" id="taskInput" placeholder="Add new task..." required />
      <button type="submit">Add</button>
    </form>
    <ul id="taskList"></ul>
  </div>

  <script>
    async function fetchTasks() {
      const res = await fetch('/tasks');
      const tasks = await res.json();
      const taskList = document.getElementById('taskList');
      taskList.innerHTML = '';
      tasks.forEach((task) => {
        const li = document.createElement('li');
        li.textContent = task.task;
        if (task.completed) li.classList.add('completed');
        li.onclick = async () => {
          await fetch(`/complete/${task.id}`, { method: 'POST' });
          fetchTasks();
        };
        taskList.appendChild(li);
      });
    }

    document.getElementById('todoForm').onsubmit = async (e) => {
      e.preventDefault();
      const input = document.getElementById('taskInput');
      await fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ task: input.value })
      });
      input.value = '';
      fetchTasks();
    };

    fetchTasks();
  </script>
</body>
</html>
