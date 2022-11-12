import {useParams} from "react-router-dom";
import Table from "react-bootstrap/Table";
import React from "react";
import {format} from 'date-fns'

const formatDate = (date) => {
    return format(new Date(date), 'dd.MM.yyyy HH:mm')
}

const TodoItem = ({todo}) => {
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
                {formatDate(todo.createdAt)}
            </td>
            <td>
                {formatDate(todo.updatedAt)}
            </td>
        </tr>
    )
}

const ProjectTodosList = ({todos}) => {
    let {id} = useParams()
    let filteredTodos = todos.filter((todo) => todo.project === +id);
    return (
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
                        Обновлена
                    </th>
                </tr>
            </thead>
            <tbody>
                {filteredTodos.map((todo) => <TodoItem key={todo.id} todo={todo}/>)}
            </tbody>
        </Table>
    )
}

export default ProjectTodosList