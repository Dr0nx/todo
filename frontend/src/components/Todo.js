import Table from "react-bootstrap/Table";
import React from "react";
import {Button} from "react-bootstrap";
import {Link} from "react-router-dom";

const TodoItem = ({todo, delete_todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.createdAt}
            </td>
            <td>
                <input type="checkbox" checked={todo.isActive}  name='isActive' />
            </td>
            <td>
                {todo.isActive ?
                    <Button onClick={() => delete_todo(todo.id)} variant="outline-danger" size="sm"
                            type='button'>Заметка в работе</Button> :
                    <Button variant="outline-success" size="sm">Заметка закрыта</Button>
                }
            </td>
        </tr>
    )
}

const TodoList = ({todos, delete_todo}) => {
    return (
        <div>
            <Table striped bordered hover>
                <thead key="thead">
                <tr>
                    <th>
                        ID проекта
                    </th>
                    <th>
                        Текст заметки
                    </th>
                    <th>
                        Автор заметки
                    </th>
                    <th>
                        Создана
                    </th>
                    <th>
                        Активна
                    </th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {todos.map((todo_, index) => <TodoItem key={index} todo={todo_} delete_todo={delete_todo}/>)}
                </tbody>
            </Table>
            <div className="row">
                <div>
                    <Link to='/todos/create'>Создать</Link>
                </div>
            </div>
        </div>
    )
}

export default TodoList